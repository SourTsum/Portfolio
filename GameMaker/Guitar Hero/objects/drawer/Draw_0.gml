if(global.selected == "darkSheep"){
	draw_text(270,414,"Dificulty: Insane");
	draw_text(270,454,"High Score: \n" + string(global.topScores[0]));
	draw_text(270,515,"Misses Allowed: 25");
}

if(global.selected == "lastingPromise"){
	draw_text(270,414,"Dificulty: Insane");
	draw_text(270,454,"High Score: \n" + string(global.topScores[1]));
	draw_text(270,515,"Misses Allowed: 10");
}

if(global.selected == "nightMonsters"){
	draw_text(270,414,"Dificulty: Easy");
	draw_text(270,454,"High Score: \n" + string(global.topScores[2]));
	draw_text(270,515,"Misses Allowed: 30");
}