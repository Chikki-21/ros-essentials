<launch>
    <node pkg="py_pkg" exec="add_two_ints_server"/>
    <node pkg="py_pkg" exec="add_two_ints_client"/>
</launch>
