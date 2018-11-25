from behave import given, when, then
from Lista import Lista


@given(u'o valor {valor}')
def given_value(context, valor):
    context.valor = valor


@when(u'criar a lista e adicionar o valor')
def when_create_list(context):
    context.lista = Lista()
    context.lista.append(context.valor)


@then(u'se o valor dentro da lista e igual a o dado na lista {itens}')
def then_itens_list(context, itens):
    print(context.lista.list_simple())
    assert context.lista.list_simple() == itens

@then(u'o ultimo item e {ultimo}')
def then_last_item(context, ultimo):
    print(f"{context.lista.ultimo_item} == {ultimo}")
    assert context.lista.ultimo_item == ultimo