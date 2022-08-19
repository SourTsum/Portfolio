if(keyboard_check(ord(global.right_keybind))){
	image_index = 1;
}
if(!keyboard_check(ord(global.right_keybind))){
	image_index = 0;
	global.canNoteT4 = true;
}