import os
from pathlib import Path
from docs_from_tests.instrument_call_hierarchy import (
    instrument_and_import_package,
    instrument_and_import_module,
    initialise_call_hierarchy,
    finalise_call_hierarchy
)
from src.hello_world_combiner import HelloWorldCombiner
from src.world import World

# you can instrument entire packages / folders at once like this
instrument_and_import_package(os.path.join(Path(__file__).parent.absolute(), '..', 'src'), 'src')
# You can instrument individual modules like this
# instrument_and_import_module('tests.blah')

# this is a wrapper around an end to end test that also outputs the documentation / sequence diagram
def test_hello_world():
    # the initialises the recording of the call hierarchy
    initialise_call_hierarchy('start')

    # This runs the actual test
    _test_hello_world()
    
    # this finalises the call hierarchy and returns the root
    root_call = finalise_call_hierarchy()

    # this returns a sequence diagram of the call hierarchy
    sequence_diagram = root_call.sequence_diagram(
        show_private_functions=False,
        excluded_functions=[
            'HelloWorldCombiner.__init__',
            'World.__init__'
        ]
    )

    # this writes out the markdown to disk    
    sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'end-to-end-sequence-diagram.md')
    Path(sequence_diagram_filename).write_text(sequence_diagram)

# this is the original / source test
def _test_hello_world():
    assert HelloWorldCombiner().combine() == 'Hello world'

# this is a wrapper around a unit test that also outputs the documentation / sequence diagram
def test_world():
    initialise_call_hierarchy('start')

    _test_world()
    
    root_call = finalise_call_hierarchy()
    #print(root_call) 
    sequence_diagram = root_call.sequence_diagram(
        show_private_functions=True,
        excluded_functions=[]
    )

    sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'world-sequence-diagram.md')
    Path(sequence_diagram_filename).write_text(sequence_diagram)

def _test_world():
    assert World().world() == 'world'



