from zope.i18nmessageid import MessageFactory

from zope import schema

from plone.directives import form, dexterity

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

_ = MessageFactory("collective.mdlevent")

class IEventCore(form.Schema):
    """Core information"""

class IEventLocation(form.Schema):
    """Where the event happens"""

    address = schema.TextLine(title=_(u"Address"))

class IEventDate(form.Schema):
    """When the event happens"""

    date = schema.Date(title=_(u"Date"))

    locations = RelationList(title=_(u"Locations"),
                 required=False,
                 default=[],
                 value_type=RelationChoice(title=_(u"Location"),
                      source=ObjPathSourceBinder(object_provides=IEventLocation.__identifier__))
                 )

