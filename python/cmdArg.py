# # Import sys module
# import sys
#
# # Print total number of arguments
# print('Total arguments:', len(sys.argv))
# print('The argument values are:', str(sys.argv))


# # Import sys module
# import sys
#
# # Print the type of the variable, sys.argv
# print(type(sys.argv))
#
# # Print each command-line argument in each line
# print('The command line arguments are:')
# for i in sys.argv:
#     print(i)

# # Import getopt module
# import getopt
# # Import sys module
# import sys
#
# # Store argument variable omitting the script name
# argv = sys.argv[1:]
#
# try:
#     # Define getopt short options
#     options, args = getopt.getopt(argv, 'x:y:')
#
#     # print the options and argument
#     print(options)
#     print(args)
#
# except getopt.GetoptError:
#
#     # Print the error message if the wrong option is provided
#     print('The wrong option is provided')
#
#     # Terminate the script
#     sys.exit(2)

# # Import getopt module
# import getopt
#
# # Import sys module
# import sys
#
# # Store argument variable omitting the script name
# argv = sys.argv[1:]
#
# # Initialize result variable
# result = 0
#
# try:
#
#     # Define getopt short and long options
#     options, args = getopt.getopt(sys.argv[1:], 'a:s', ['add=', 'sub='])
#
#     # Read each option using for loop
#     for opt, arg in options:
#         # Calculate the sum if the option is -a or --add
#         if opt in ('-a', '--add'):
#             result = int(argv[1]) + int(argv[2])
#
#         # Calculate the suntraction if the option is -s or --sub
#         elif opt in ('-s', '--sub'):
#             result = int(argv[1]) - int(argv[2])
#
#     print('Result = ', result)
#
# except getopt.GetoptError:
#
#     # Print the error message if the wrong option is provided
#     print('The wrong option is provided')
#
#     # Terminate the script
#     sys.exit(2)


# Import argparse module
import argparse

# Import sys module
import sys


# Declare function to define command-line arguments
def readOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="The parsing commands lists.")
    parser.add_argument("-n", "--name", help="Type your name.")
    parser.add_argument("-e", "--email", help="Type your email.")
    opts = parser.parse_args(args)
    return opts


# Call the function to read the argument values
options = readOptions(sys.argv[1:])
print(options.name)
print(options.email)
