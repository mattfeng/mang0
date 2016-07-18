class Feature(object):
    def __init__(self, name, dist_folder, description):
        self.name = name
        self.desc = description
        self.updates = []

        dist_folder = dist_folder.rstrip('/') + '/'  # ensure there is a / at the end
        with open(dist_folder + 'updates.dist') as f:
            info = f.readline().strip()             # info such as 'time-series'
            for line in f:
                line = line.strip().split(' ')
                time_to_update = float(line[0])
                updated_dist = dist_folder + line[1]
                self.updates.append((time_to_update, updated_dist))

        self.generator = None