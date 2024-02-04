
default time = Time()
default selected_location = Place.HOME_MC_ROOM

image img_black = Solid("#000000")

screen game_screen(location):
    window id "game_screen"
    add location.background

    hbox:
        align (1.0, 0.0)
        for next_location in location.accessible_locations:
            imagebutton:
                idle next_location.icon
                hover next_location.icon
                action Return(next_location)

label game_loop:
    $ current_location = locations[selected_location]
    $ next_event = current_location.get_event(time)
    while next_event:
        call expression next_event.label pass next_event
        $ result = _return
        if next_event != result:
            $ next_event = result
        else:
            $ next_event = None

    call screen game_screen(current_location) nopredict
    $ result = _return
    if 'next_location' in result:
        $ selected_location = result['next_location']

    jump game_loop

