# use this to detect motion in the room, make a note of when the last detected motion was
# locally on the node rather than the server to negate the need for the server to save the
# node data locally, using persitant data store, i.e. a log file with the time saved

def get_live_data()