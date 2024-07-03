from gym import envs
import gym_pcgrl

for env in envs.registry.values():
    if "gym_pcgrl" in env.entry_point:
        print(env.id)
