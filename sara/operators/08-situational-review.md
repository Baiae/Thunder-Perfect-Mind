# Lesson Review Protocol

Invoked to surface due lessons throughout the day. Spaced repetition in practice.

## REV-01 · Surface One or Two
Retrieve lessons where review is due (due_at ≤ now). Return one, or at most two. The point is recall practice, not cramming. If more than five are due, surface the two with the oldest due dates first.

## REV-02 · Present, Then Ask
Show the lesson text. Then ask: "Does this still hold? Any updates?" If Phaedra confirms it's still accurate, advance the review interval. If she updates or contradicts it, record the revision and reset the interval to 1 day.

## REV-03 · Mark and Schedule
After each review: update last_seen_at to now. If the lesson held, advance to the next rung on the spaced-repetition ladder (1→3→7→21→60). If it was revised, restart at 1 day. A lesson revised three times may need to be replaced, not extended.
