from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

class SnacksTest(TestCase):
  def setUp(self):
    self.user = get_user_model().objects.create_user(
        username="tester", email="tester@email.com", password="pass"
    )

    self.snack = Snack.objects.create(
        title="Fresca", description="Sparkling Soda Water", purchaser=self.user,
    )

  def test_list_status(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_list_template(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'snack_list.html')
    self.assertTemplateUsed(response, 'base.html')

  def test_list_page_context(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    snacks = response.context['snack_list']
    self.assertEqual(len(snacks), 1)
    self.assertEqual(snacks[0].title, "Fresca")
    self.assertEqual(snacks[0].purchaser.username, "tester")

  def test_detail_page_status_code(self):
    url = reverse('snack_detail',args=(1,))
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_detail_page_template(self):
    url = reverse('snack_detail',args=(1,))
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'snack_detail.html')
    self.assertTemplateUsed(response, 'base.html')
    
  def test_detail_page_context(self):
      url = reverse('snack_detail',args=(1,))
      response = self.client.get(url)
      snack = response.context['snack']
      self.assertEqual(snack.title, "Fresca")
      self.assertEqual(snack.purchaser.username, "tester")

  def test_create_status(self):
    url = reverse('snack_create')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_create_template(self):
    url = reverse('snack_create')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'snack_create.html')
    self.assertTemplateUsed(response, 'base.html')

  def test_update_status(self):
    url = reverse('snack_update', args=(1,))
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_update_template(self):
    url = reverse('snack_update', args=(1,))
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'snack_update.html')
    self.assertTemplateUsed(response, 'base.html')

  def test_delete_status(self):
    url = reverse('snack_delete', args=(1,))
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_delete_template(self):
    url = reverse('snack_delete', args=(1,))
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'snack_delete.html')
    self.assertTemplateUsed(response, 'base.html')