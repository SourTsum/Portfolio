if(keyboard_check(ord(global.right_mid_keybind))){
	image_index = 1;
}
if(!keyboard_check(ord(global.right_mid_keybind))){
	image_index = 0;
	global.canNoteT3 = true;
}