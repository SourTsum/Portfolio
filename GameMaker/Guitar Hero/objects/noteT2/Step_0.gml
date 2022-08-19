image_xscale += (speed/1000);
image_yscale += (speed/1000);
speed+= 0.008 + global.speedNote;

if(y > 800){
	if(global.miss > 0){
		global.miss -= 1;
	}
	instance_destroy();
}

if(instance_place(x,y,inputNoteT2) && keyboard_check(ord(global.left_mid_keybind)) && global.canNoteT2 == true){
	global.canNoteT2 =  false;
	instance_destroy();
	rnDistance = (ecludianDistance(x,y,inputNoteT2.x,inputNoteT2.y))
	if(rnDistance <= 35){
		global.thisScore += 210;
	}
	else{
		if(rnDistance <= 45){
			global.thisScore += 166;
		}else{
			if(rnDistance <= 75){
				global.thisScore += 45;
			}
		}
	}
}