from pony import orm

db = orm.Database()


def _append_sub_dict(parent_dict, table, sub_dict_name):
    if table.count():
        parent_dict[sub_dict_name] = []
        for e in table.select():
            parent_dict[sub_dict_name].append(e.to_dict())

class Question(db.Entity):
    _table_ = 'Questions'

    title = orm.Required(unicode)
    code = orm.Optional(unicode)
    # TODO: validate type
    type = orm.Required(str)  # choice, multi, text, code, hidden
    # TODO: validate choice
    choices = orm.Optional(unicode)  # only for choice, multi
    error = orm.Optional(unicode)

    pages = orm.Set('Page')


class Action(db.Entity):
    _table_ = 'Actions'

    title = orm.Required(unicode)
    # TODO: validate type
    type = orm.Required(str)  # 'get', 'post' or 'both'
    url = orm.Required(unicode)

    _submit_for = orm.Optional('Page', reverse='submit')
    pages = orm.Set('Page', reverse='actions')


class Page(db.Entity):
    _table_ = 'Pages'

    path = orm.Required(unicode, unique=True)
    title = orm.Optional(unicode)
    description = orm.Optional(unicode)
    error = orm.Optional(unicode)
    questions = orm.Set('Question')
    submit = orm.Optional('Action')
    actions = orm.Set('Action')

    def to_dict(self, *args, **kwargs):
        ret_dict = super(Page, self).to_dict(*args, **kwargs)
        _append_sub_dict(ret_dict, self.actions, 'actions')
        _append_sub_dict(ret_dict, self.questions, 'questions')
        return ret_dict

