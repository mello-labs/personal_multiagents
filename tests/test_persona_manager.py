def test_persona_manager_loads_and_sets_active(monkeypatch):
    from agents import persona_manager

    monkeypatch.setattr(
        persona_manager,
        "_active_persona_id",
        persona_manager._DEFAULT_PERSONA_ID,
        raising=False,
    )

    persona_manager.reload_personas()
    personas = persona_manager.list_personas()

    assert personas
    assert any(p["id"] == persona_manager._DEFAULT_PERSONA_ID for p in personas)

    first_id = personas[0]["id"]
    assert persona_manager.set_active_persona(first_id) is True
    assert persona_manager.get_active_persona_id() == first_id

    assert persona_manager.set_active_persona("missing-persona") is False
    assert persona_manager.get_active_persona_id() == first_id

    fallback = persona_manager.get_persona("missing-persona")
    assert fallback.get("id") == persona_manager._DEFAULT_PERSONA_ID


def test_persona_manager_temperature_defaults():
    from agents import persona_manager

    persona_manager.reload_personas()
    temperature = persona_manager.get_temperature("coordinator", "direct")

    assert isinstance(temperature, float)


def test_persona_manager_prefere_sanity_quando_persona_existe(monkeypatch):
    from agents import persona_manager

    monkeypatch.setattr(
        persona_manager.sanity_client,
        "get_all_personas",
        lambda: [
            {
                "name": "Coordenador Sanity",
                "persona_id": {"current": "coordinator"},
                "short_name": "Coord+",
                "icon": "◎",
                "description": "Versão governada no Studio",
                "tone": "warm",
                "system_prompt": "Prompt vindo do Sanity",
                "synthesis_prompt_override": "Síntese do Sanity",
                "direct_prompt_override": "Direto do Sanity",
                "parameters": {"temperature_direct": 0.11},
                "active": True,
            }
        ],
    )
    monkeypatch.setattr(persona_manager.sanity_client, "invalidate_cache", lambda: None)

    persona_manager.reload_personas()
    persona = persona_manager.get_persona("coordinator")

    assert persona["name"] == "Coordenador Sanity"
    assert persona["icon"] == "◎"
    assert persona_manager.get_direct_prompt("coordinator") == "Direto do Sanity"
    assert persona_manager.get_temperature("coordinator", "direct") == 0.11
