/// @DnDAction : YoYo Games.Drawing.Set_Font
/// @DnDVersion : 1
/// @DnDHash : 00737DF5
/// @DnDArgument : "font" "scoreFont"
/// @DnDSaveInfo : "font" "scoreFont"
draw_set_font(scoreFont);

/// @DnDAction : YoYo Games.Drawing.Draw_Value
/// @DnDVersion : 1
/// @DnDHash : 62B45116
/// @DnDArgument : "x" "200"
/// @DnDArgument : "y" "243"
/// @DnDArgument : "caption" ""
/// @DnDArgument : "var" "global.thisScore"
draw_text(200, 243,  + string(global.thisScore));