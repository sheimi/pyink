# flags: --preview --line-length=80 --pyink --pyink-indentation=2
a_very_long_library_name._private_method(and_a_long_arg)  # pylint: disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # pylint: disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # pylint: disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_no_long_fits_______)  # pylint: disable=protected-access

a = a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_____)  # pylint: disable=protected-access


class MyDataclass:
  some_field: module.SomeClass[int] = DefaultValue  # pytype: disable=annotation-type-mismatch

# output

a_very_long_library_name._private_method(and_a_long_arg)  # pylint: disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit_)  # pylint: disable=protected-access
a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_limit___)  # pylint: disable=protected-access
a_very_long_library_name._private_method(
    and_a_long_arg_that_no_long_fits_______
)  # pylint: disable=protected-access

a = a_very_long_library_name._private_method(and_a_long_arg_that_just_fits_____)  # pylint: disable=protected-access


class MyDataclass:
  some_field: module.SomeClass[int] = DefaultValue  # pytype: disable=annotation-type-mismatch
