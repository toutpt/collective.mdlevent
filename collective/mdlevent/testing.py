from plone.testing import z2

from plone.app.testing import *
import collective.mdlevent

FIXTURE = PloneWithPackageLayer(zcml_filename="configure.zcml",
                                zcml_package=collective.mdlevent,
                                additional_z2_products=[],
                                gs_profile_id='collective.mdlevent:default',
                                name="collective.mdlevent:FIXTURE")

INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                        name="collective.mdlevent:Integration")

FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                        name="collective.mdlevent:Functional")

