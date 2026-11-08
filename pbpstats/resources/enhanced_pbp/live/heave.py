from pbpstats.resources.enhanced_pbp.live.field_goal import LiveFieldGoal


class LiveHeave(LiveFieldGoal):
    """
    Class for heave events (actionType "heave"), new in the 2025-26 live data.

    From 2025-26 the NBA no longer charges missed end-of-quarter heaves to the
    shooter. The live feed logs them as a team-level event (personId 0, no
    shotResult), followed by a rebound whose shotActionNumber points at it. Made
    heaves are still logged as ordinary 3pt field goals.

    Treated here as a missed 3 by "team" (player id 0): possessions and rebounds work
    as for any missed shot, team and lineup stats include the attempt, and no real
    player is credited with it, matching NBA.com's official player stats.

    From 2026-27 the feed also names the shooter (personId). It is kept as
    heave_shooter_id but not credited, so all seasons are treated the same.
    """

    action_type = ["heave"]

    def __init__(self, *args):
        super().__init__(*args)
        self.heave_shooter_id = getattr(self, "player1_id", 0) or 0
        self.player1_id = 0

    @property
    def shot_value(self):
        return 3

    @property
    def is_made(self):
        return False

    @property
    def is_corner_3(self):
        return False
