from elevator_system.elevator import Elevator


def test_create_elevator():
    elevator = Elevator()

    assert elevator.current_floor == 0

    assert elevator.door_is_open is False
