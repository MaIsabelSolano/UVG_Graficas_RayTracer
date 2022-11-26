class Material:
    def __init__(self, diffuse, albedo = [1, 0, 0, 0], spec = 0, refractive_index = 0, texture = None):
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec
        self.refractive_index = refractive_index
        self.texture = None