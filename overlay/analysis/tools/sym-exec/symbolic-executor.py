#!/usr/bin/env python2

import os
import sys

import angr
import claripy
import simuvex


# Run a basic symbolic execution.
def detect_symbolic_input(proj, start_from, target):
    # size of symbolic buffer (input buffer, 5 bytes)
    # DO NOT change this.
    sym_arg_size = 5
  
    # create buffer by multiplying it with 8 ( 8 bits in each byte )
    # DO NOT change this.
    sym_buf = claripy.BVS('sym_buffer_' + str(start_from), sym_arg_size * 8)

    # set start address as starting point, set symbolic buffer as
    # its argument.
    # DO NOT change this
    init = proj.factory.call_state(start_from, sym_buf)

    # set constratins
    for each_byte in sym_buf.chop(8):
        # printable character.
        # CHANGE THIS: Please fix the constraints to find the commands,
        #              which consist of all in capital letters...
        init.add_constraints(each_byte >= 0x20)
        init.add_constraints(each_byte <= 0x7f)

    # init path group for the binary (DO NOT CHANGE)
    path_group = proj.factory.path_group(init)

    # set target, and try to explore the path! (DO NOT CHANGE)
    ex = path_group.explore(find=target, avoid=None)

    # if any path found, return the results.
    return_arr = []
    if len(ex.found) > 0:
      for i in xrange(len(ex.found)):
        concretized_input = ex.found[i].state.se.any_str(sym_buf)
        return_arr.append(concretized_input[0:4])
    else:
        pass
        #"Cannot find input for 0x%08x" % target...
    return return_arr

def main():
    # check binary (DO NOT CHANGE)
    binary_name = sys.argv[1]
    if not os.path.exists(binary_name):
      print("Error: binary does not exist at %s" % binary_name)
      quit()

    print("Binary: %s" % binary_name)

    # loader options (DO NOT CHANGE)
    l_options = {}
    l_options['auto_load_libs'] = False

    # load binary (DO NOT CHANGE)
    try:
      proj = angr.Project(binary_name,  load_options=l_options)
    except:
      print("Binary load failed: %s" % binary_name)
      quit()

    # read data sheet (DO NOT CHANGE)
    with open('functions.txt','rb') as f:
      data = f.read()
      f.close()

    # get the list of functions (DO NOT CHANGE)
    functions_list = eval(data)

    # run symbolic execution
    # FIXME: run symbolic execution to all functions in the list
    #        to get the correct command for the malware
    #        A hint: all command strings are 4 characters, and
    #                all those characters are in upper case
    #                (capital letters).
    #                There are 2 legitimate commands, you need to 
    #                run the malware with the commands to find the 
    #                correct commands from upper case commands...

    # example of symbolic execution...
    func_addr = functions_list[0]
    # contains start and end address as a tuple = (start, end)
    print(func_addr)
    
    # run the symbolic execution from start (func_addr[0]) to end (func_addr[1]) address
    result = detect_symbolic_input(proj, func_addr[0], func_addr[1])
    print(result)


# DO NOT CHANGE THIS
if __name__ == '__main__':

  if(len(sys.argv) != 2):
    print("Usage: %s [target-program]" \
          % sys.argv[0])
    quit()

  main()
