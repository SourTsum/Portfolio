time = audio_sound_get_track_position(const);

if(keyboard_check_released(ord("Z"))){
	T1[indexes[0]] = time;
	indexes[0] += 1;
}
if(keyboard_check_released(ord("X"))){
	T2[indexes[1]] = time;
	indexes[1] += 1;
}
if(keyboard_check_released(188)){
	T3[indexes[2]] = time;
	indexes[2] += 1;
}
if(keyboard_check_released(190)){
	T4[indexes[3]] = time;
	indexes[3] += 1;
}

if(audio_is_playing(const) == false && alarm[0] == -1){
	show_debug_message(T1);
	show_debug_message(T2);
	show_debug_message(T3);
	show_debug_message(T4);
	game_end();
}