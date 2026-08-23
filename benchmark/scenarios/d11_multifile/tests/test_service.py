from src.service import TodoService


def test_create():
    svc = TodoService()
    t = svc.create("buy milk")
    assert t.id == 1
    assert t.title == "buy milk"
    assert t.done is False


def test_create_rejects_empty():
    svc = TodoService()
    import pytest
    with pytest.raises(ValueError):
        svc.create("")
    with pytest.raises(ValueError):
        svc.create("   ")


def test_complete():
    svc = TodoService()
    t = svc.create("write tests")
    svc.complete(t.id)
    assert svc.store.get(t.id).done is True


def test_pending_and_done():
    svc = TodoService()
    a = svc.create("task a")
    b = svc.create("task b")
    c = svc.create("task c")
    svc.complete(b.id)
    pending = svc.pending()
    done = svc.done()
    assert {t.id for t in pending} == {a.id, c.id}
    assert {t.id for t in done} == {b.id}


def test_delete():
    svc = TodoService()
    t = svc.create("delete me")
    assert svc.store.delete(t.id).id == t.id
    assert svc.store.get(t.id) is None
