from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Parent, Child

"""
Some helper methods to create parents and children
"""

def _create_parent(firstname, surname, age):
    return Parent.objects.create(firstname=firstname, 
                                surname=surname, age=age)

def _create_child(firstname, surname, age, parent):
    return Child.objects.create(firstname=firstname, surname=surname, 
                                age=age, parent=parent)

"""
Test the parent and child views
"""
class ParentChildViewTests(TestCase):

    def test_parent_view_no_parents(self):
        response = self.client.get(reverse('pc:parents'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'parent_child_app/parents.html')
        self.assertContains(response, 'There are no parents yet.')

    def test_parent_view_with_parents(self):
        _create_parent('Fred', 'Bloggs', 32)

        response = self.client.get(reverse('pc:parents'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'parent_child_app/parents.html')
        self.assertContains(response, 'Fred')
        self.assertQuerysetEqual(response.context['parent_list'], 
                                ['<Parent: Fred>']) # from __str__ method of model
        self.assertEqual(Parent.objects.count(), 1)

    def test_child_view_no_children(self):
        parent = _create_parent('Brigitte', 'Smith', 24)
        response = self.client.get(reverse('pc:children', args=(parent.id,)))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'parent_child_app/children.html')
        self.assertContains(response, 'There are no children yet.')

    def test_child_view_with_children(self):
        parent = _create_parent('Trevor', 'Jones', 41)
        child = _create_child('Toby', 'Jones', 4, parent)

        response = self.client.get(reverse('pc:children', args=(parent.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'parent_child_app/children.html')
        self.assertContains(response, 'Children of Trevor Jones')

        self.assertQuerysetEqual(response.context['child_list'], 
                                ['<Child: Toby>'])

        self.assertContains(response, 'Toby who is 4')

