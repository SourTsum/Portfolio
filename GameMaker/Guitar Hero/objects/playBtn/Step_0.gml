if (distance_to_point(mouse_x,mouse_y) <= 0)
{
    image_index = 1
    if (image_xscale < scale_max){
        image_xscale += scale_speed
        image_yscale += scale_speed
    }
}
else
{
    image_index = 0
    if (image_xscale > 1){
        image_xscale -= scale_speed
        image_yscale -= scale_speed
    }
}
