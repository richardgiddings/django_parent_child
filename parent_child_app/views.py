from django.shortcuts import render_to_response
from .models import Parent, Child

def parents(request):
    """
    Return the parents
    """
    parent_list = Parent.objects.order_by('firstname')

    return render_to_response('parent_child_app/parents.html',
                            {'parent_list': parent_list})


def children(request, parent_id):
    """
    Return the children of a parent
    """
    child_list = Child.objects.filter(parent=parent_id).order_by('firstname')
    parent = Parent.objects.get(id=parent_id)

    return render_to_response('parent_child_app/children.html',
                            {'child_list': child_list,
                             'parent': parent})
