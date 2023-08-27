class FriendGroup:
    def __init__(self):
        self.representative = self
        self.size = 1


def make_friendship(group1, group2):
    group1_root = friend_find(group1)
    group2_root = friend_find(group2)
    if group1_root == group2_root:
        return group1_root.size
    elif group1_root.size > group2_root.size:
        group2_root.representative = group1_root
        group1_root.size += group2_root.size
        return group1_root.size
    else:
        group1_root.representative = group2_root
        group2_root.size += group1_root.size
        return group2_root.size


def friend_find(current_group):
    if current_group.representative == current_group:
        return current_group
    else:
        current_group.representative = friend_find(current_group.representative)
        return current_group.representative


def friend_tracker(new_friends, friendship_dict):
    friend1, friend2 = new_friends.split(" ")
    if friend1 not in friendship_dict:
        friendship_dict[friend1] = FriendGroup()
    if friend2 not in friendship_dict:
        friendship_dict[friend2] = FriendGroup()
    print(make_friendship(friendship_dict[friend1], friendship_dict[friend2]))


testcases = int(input())
for i in range(testcases):
    friendships = int(input())
    friendship_dict = {}
    for friends in range(friendships):
        new_friends = input()
        friend_tracker(new_friends, friendship_dict)
