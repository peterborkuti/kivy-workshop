0000 minimal app

0010 root widget in kv file. kv: Button,Label,Boxlayout
Try different layouts :https://kivy.org/docs/gettingstarted/layouts.html

0012 interactivity in kv file, changing same element
Try different UX widgets: https://kivy.org/docs/api-kivy.uix.html
Try some of its properties

0020 id in kv file, changing sibling element

0030 no root widget nor in kv nor in py file

0032 creating root widget in py with build (Button)

0035 Instantiate root widget in py, class rule in kv

0037 Interactivity, Button on_press in kv, with self.press (BAD! see error message, so what is self pointing to?)

0038 root.pressed but only in kv file. Check error message!

0039 Creating pressed method in MyWidget class in py file.
Display the value of an input field in a label
Disable an input field based on a checkbox
Put a textbox and a label. Display the cursor coordinates in the label.
Put a textbox. When user hit enter, a popup should come up with the text "Thank you" (0500)

00100 Canvas
http://robertour.com/2013/07/19/10-things-you-should-know-about-the-kivy-canvas/

00110 Canvas is not a widget, it has no size. Canvas is a set of instruction. The Widget itself has a size
 and the Ellipse also has a default size.
 
00120 Button is also a widget and it has a canvas, you can draw on it...

00130 Botton has no attribute 'r'

00132 MyWidget has no attribute 'r'

00134 It runs, but does nothing fancy. What if Button presses changes color?

00136 When button pressed, circle's color changes

00140 Interactivity with canvas: on_touch_down event

00142 Circle is drown on touch position. Seems to be OK, but not. It positions the whole widget, not the ellipse

00144 A bit better positioning

00150 Clock

00160 Move circle to the touch point
