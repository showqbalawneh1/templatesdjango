from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape,mark_safe, escape

register = template.Library()

# الاستعمال الصح decorator
# ممكن يكون في طريقة ثانية نستعملها انو بس هاي ال recommended 
# هاي bestpractice 
@register.filter
def lower (value):
    return value.lower


@register.filter
def first_letter(iterator):
    result = ""
    for item in iterator:
        result+= item[0]
    return result
#  بضيفها اذا كان الاسم غير عن اسم  الميثود 
# @register.filter(name="nth_letter", is_safe=True)
# def other_letters(itrable , num ):
#     return "hihi"


@register.filter(name="nth_letters", is_safe=True)
def other_letters(iterable, num):
    result=" "
    for item in iterable :
        if len(item) < num or not item[n-1 ].isalpha():
            result+=" "
        else: 
            result+=item[n-1]
            
    return result

@register.filter(needs_autoescape= True)
@stringfilter
def letter_count(value, letter , autoescape = True):
    if autoescape:
        value=conditional_escape(value)
        result = (
            f"<i>(value)</i> has <b> {value.count(letter)}</b>"
            f"instance(s) of the letter <b> {letter}</b>"
        )
        return mark_safe(result)
    

@register.simple_tag
def make_ul(iterable):
    content = ["<ul>"]
    for item in iterable:
        content.append(f"<li>{escape(item)}</li>")
    content.append("</ul>")
    content = "".join(content)
    return mark_safe(content)
#معناها الداتا اللي بيبعتها ال
# takes context  -> بتعني انو الكونتست من الview  بيقدر يوصلها 
#takes_context --> بتاخد الكونتست من ال view direct 
@register.simple_tag(takes_context=True)
def dino_list(context, title):
    output = [f"<h2>{title}</h2><ul>"]
    for dino in context["dinosaurs"]:
        output.append(f"<li>{escape(dino)}</li>")
    output.append("</ul>")
    output = "".join(output)
    context["weight"] = "20 tons"
    return mark_safe(output)



@register.simple_tag
def mute(*args):
    return ""