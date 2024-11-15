#!/usr/bin/python3
"""Solve the lock boxes puzzle by determining if all boxes can be unlocked."""


def look_next_opened_box(opened_boxes):
    """Search for the next unlocked box and retrieve its keys.    
    Args:
        opened_boxes (dict): Dictionary representing
        opened boxes, with their keys.
    Returns:
        list: A list of keys found in the next opened box,
        or None if all boxes have been checked.
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Determine if all boxes in a sequence can
    be unlocked using available keys.
    Args:
        boxes (list): A list of lists where
        each sublist contains keys for other boxes.
    Returns:
        bool: True if all boxes can be unlocked; otherwise, False.
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    aux = {}
    while True:
        if len(aux) == 0:
            aux[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = look_next_opened_box(aux)
        if keys:
            for key in keys:
                try:
                    if aux.get(key) and \
                            aux.get(key).get('status') == 'opened/checked':
                        continue
                    aux[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in aux.values()]:
            continue
        elif len(aux) == len(boxes):
            break
        else:
            return False

    return len(aux) == len(boxes)


def main():
    """Entry point for the lock boxes puzzle solution."""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
