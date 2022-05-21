"""
Grain:
    Phenocryst:
        id: particle.reference.name
        locations: Location references
        owner: identity
        aes: 123...
    Particle:
        content

    particle + particle == Grain(0)
    Grain(x) + particle == Grain(x)
    Grain(x) + Grain(y) == Grain(z) == xy

"""
