image_xscale += (speed/1000);
image_yscale += (speed/1000);
speed+= 0.008 + global.speedNote;
if(y > 800){
	if(global.miss > 0){
		global.miss -= 1;
	}
	instance_destroy();
}
if(instance_place(x,y,inputNoteT3) && keyboard_check(ord(global.right_mid_keybind)) && global.canNoteT3 == true){
	global.canNoteT3 = false;
	instance_destroy();
	rnDistance = (ecludianDistance(x,y,inputNoteT3.x,inputNoteT3.y))
	if(rnDistance <= 6){
		global.thisScore += 210;
	}
	else{
		if(rnDistance <= 21){
			global.thisScore += 166;
		}else{
			if(rnDistance <= 45){
				global.thisScore += 45;
			}
		}
	}
}