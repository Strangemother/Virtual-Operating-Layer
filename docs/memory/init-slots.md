# Slots

Memory 'slots' provide static dacades within the memory module, assigned to unique names. The memory reference is manipulated through the branded location - the addresses beneath are hidden.

    memory.slot('user', UserFacade)

    user = memory.get_slot('user')
    user.uname
    # 'username'
    user.uname = 'newuser'
    # Error: Cannot write slot "user"
