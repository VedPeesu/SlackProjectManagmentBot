import unittest
from main import app 
class SlackBotTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_assign_task(self):
        response = self.client.post('/assign-task', data={'text': '1 user4'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Task '1' has been assigned to 'user4'.", response.data)
    
    def test_unassign_task(self):
        response = self.client.post('/unassign-task', data={'text': '1'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Task '1' has been unassigned.", response.data)
    
    def test_create_project_summary(self):
        response = self.client.post('/create-project-summary', data={'text': 'Project Design, Example summary.'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Project summary for 'Project Design'", response.data)

    def test_list_project_summaries(self):
        self.client.post('/create-project-summary', data={'text': 'Project A, Summary A'})
        response = self.client.post('/list-project-summaries')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Project Summaries:", response.data)

    def test_notify_me(self):
        response = self.client.post('/notify-me', data={'text': 'Meeting, 12:45', 'user_id': 'exampleuser', 'channel_id': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Reminder set for", response.data)
    
    def test_create_task(self):
        response = self.client.post('/create-task', data={'text': 'Test task'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Task created: Test task. Task ID:", response.data)    
    
    def test_set_task_priority(self):
        self.client.post('/create-task', data={'text': 'Test task'})
        response = self.client.post('/task-priority', data={'text': '1 High'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Priority for task ID 1 updated to High.", response.data)

    def test_list_tasks(self):
        self.client.post('/create-task', data={'text': 'Test task'})
        response = self.client.post('/list-tasks')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Tasks:", response.data)

    def test_clear_tasks(self):
        self.client.post('/create-task', data={'text': 'Test task'})
        response = self.client.post('/clear-tasks')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"All tasks have been cleared.", response.data)

    def test_set_reminder(self):
        response = self.client.post('/set-reminder', data={'text': 'Example reminder', 'user_id': 'exampleuser', 'channel_id': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Reminder set for 24 hours: Example reminder", response.data)

if __name__ == '__main__':
    unittest.main()