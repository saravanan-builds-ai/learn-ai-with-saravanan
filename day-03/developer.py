from dataclasses import dataclass, field


@dataclass(frozen=True)
class Developer:
    name: str
    experience: int
    skills: list[str]= field(default_factory=list)
    def add_skill(self, skill: str):
        self.skills.append(skill)