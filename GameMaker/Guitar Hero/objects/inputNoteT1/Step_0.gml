if(keyboard_check(ord(global.left_keybind))){
	image_index = 1;
}
if(!keyboard_check(ord(global.left_keybind))){
	image_index = 0;
	global.canNoteT1 = true;
}