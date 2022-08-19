if(global.drawScore == true && global.highschore == true){
	draw_set_halign(fa_center);
	draw_text(685,330,"Song Overs\nYou will be sent back shortly\nYour score was: " + string(global.thisScore) + "\nHIGH-SCORE\n\nYOU WON!");
}
if(global.drawScore == true and !(global.highschore == true)){
	draw_set_halign(fa_center);
	draw_text(685,330,"Song Overs\nYou will be sent back shortly\nYour score was: " + string(global.thisScore) + "n\nYOU WON!");	
}

if(global.miss == 0){
	draw_set_halign(fa_center);
	draw_text(685,330,"Game Over\n(You lost)\nBetter luck next time!");	
}