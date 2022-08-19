curTime = audio_sound_get_track_position(const);

if(indexes[0] < array_length(stampsT1) && curTime >= (stampsT1[indexes[0]])-1){
	instance_create_layer(x,y,0,noteT1);
	indexes[0] += 1;
}
if(indexes[1] < array_length(stampsT2) && curTime >= (stampsT2[indexes[1]])-1){
	instance_create_layer(x,y,0,noteT2);
	indexes[1] += 1;
}
if(indexes[2] < array_length(stampsT3) && curTime >= (stampsT3[indexes[2]])-1){
	instance_create_layer(x,y,0,noteT3);
	indexes[2] += 1;
}
if(indexes[3] < array_length(stampsT4) && curTime >= (stampsT4[indexes[3]])-1){
	instance_create_layer(x,y,0,noteT4);
	indexes[3] += 1;
}

if(curTime == 0 && global.thisScore >= 1 || global.miss == 0){
	if(global.topScores[0] <= global.thisScore && global.miss != 0){global.highschore = true};
	global.topScores[0] = max(global.topScores[0],global.thisScore);
	if(alarm[0] == -1){
		if(global.miss != 0){
			global.drawScore = true;
		}
		alarm[0] = room_speed * 3;		
	}
	audio_stop_all();
}