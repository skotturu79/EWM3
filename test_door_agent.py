import unittest

from door_agent import DoorAgent


class DoorAgentTests(unittest.TestCase):
    def test_defaults_to_closed_and_locked(self):
        agent = DoorAgent()
        self.assertFalse(agent.is_open)
        self.assertTrue(agent.is_locked)
        self.assertEqual(agent.status, "closed_locked")

    def test_cannot_open_when_locked(self):
        agent = DoorAgent()
        self.assertFalse(agent.request_open())
        self.assertEqual(agent.status, "closed_locked")

    def test_unlock_then_open(self):
        agent = DoorAgent()
        self.assertTrue(agent.request_unlock())
        self.assertTrue(agent.request_open())
        self.assertEqual(agent.status, "open")

    def test_cannot_lock_when_open(self):
        agent = DoorAgent(is_open=True, is_locked=False)
        self.assertFalse(agent.request_lock())
        self.assertEqual(agent.status, "open")

    def test_close_then_lock(self):
        agent = DoorAgent(is_open=True, is_locked=False)
        self.assertTrue(agent.request_close())
        self.assertTrue(agent.request_lock())
        self.assertEqual(agent.status, "closed_locked")


if __name__ == "__main__":
    unittest.main()
