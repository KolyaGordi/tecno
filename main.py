
import flet as ft
import time
import random
import json

with open(r'tree\assets\qwest — копия.json', 'r',encoding='utf-8' ) as file:
    data=json.load(file)
n=0
 
def qwests(): 
    global data 
    qwest=random.choice(list(data.keys())) 
    no= data[qwest][1] 
    anses=list(data[qwest][0]) 
 
    true=anses.pop(2)[1:-1] 
    anses.append(true) 
    random.shuffle(anses) 
    data.pop((qwest)) 
    
    true=anses.index(true) 
    return qwest,anses,true,no 

def main(page: ft.Page):
    page.title = "Техноелка Т191"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    #page.bgcolor=ft.colors.SURFACE_VARIANT
    page.theme_mode = ft.ThemeMode.LIGHT

    
    


        


    class we():
        def __init__(self,e):
            self.e=e
            self.qw,self.ans,self.tr,self.n=qwests()
            self.btnans=None
            self.row1=ft.Row([ft.Radio(value=0, label=self.ans[0],active_color='black',label_style=ft.TextStyle(size=15)),ft.Text(value='',size=20)],)
            self.row2=ft.Row([ft.Radio(value=1, label=self.ans[1],active_color='black',label_style=ft.TextStyle(size=15)),ft.Text(value='',size=20)],)
            self.row3=ft.Row([ft.Radio(value=2, label=self.ans[2],active_color='black',label_style=ft.TextStyle(size=15)),ft.Text(value='',size=20)],)
            
            self.ansgroup=ft.RadioGroup(content=ft.Column([self.row1,self.row2,self.row3]),value=0)

            self.non=ft.Text(value='',size=15,offset=ft.transform.Offset(-0.25,0),opacity=0, animate_opacity=500, animate_offset=ft.animation.Animation(800,ft.AnimationCurve.BOUNCE_OUT))
            
            self.btnans=ft.ElevatedButton(content=ft.Text('Проверить',size=20,color='black'), bgcolor=ft.colors.CYAN_ACCENT_200,height=30,width=page.width,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),on_click=self.tru)
            self.ansans=ft.Text(value='',size=20)
        
            
            
            self.inner_content = ft.Container(content=ft.Column(controls=[self.ansans,self.ansgroup,self.btnans]), bgcolor='#D1FAFA',
                expand=True,
                border_radius=10,
                padding=40)
        

            self.outer_container = ft.Container(
                content= self.inner_content,
                image_fit=ft.ImageFit.COVER,
                border_radius=10,
                padding=10,
                image_src='fon_cont.png',
                offset=ft.transform.Offset(0,0.25),
                animate_offset=ft.animation.Animation(800),
                animate_opacity=300,
                opacity=0)

        def p(self,e=1):
            page.clean()
            
        
           
        
            
            self.ansans.value=self.qw
            page.add(
            appbar,self.outer_container)
            page.update()
            time.sleep(0.3)
            self.outer_container.opacity=1
            self.outer_container.offset=ft.transform.Offset(0,0)
            page.update()

        def tru(self,e=1):
            t=int(self.ansgroup.value)


            
            for i in range(3):
                self.l=[self.row1,self.row2,self.row3]
                self.l[i].controls[1]=ft.Text(value=self.ans[i],size=20)
                if i != self.tr:

                    if i == t: 
                        self.e.icon=ft.icons.BLOCK_SHARP
                        self.e.padding=0
                        self.e.icon_color=ft.colors.DEEP_ORANGE_ACCENT_400

                        self.l[i].controls[0] = ft.Stack([
                            ft.Icon(name=ft.icons.CIRCLE_OUTLINED, size=25, color='blue'),
                            ft.Icon(name=ft.icons.DO_NOT_DISTURB_ON_OUTLINED, size=18, color='red')
                        ], alignment    =ft.alignment.center)
  
                    else:


                            self.l[i].controls[0] = ft.Row([
                            ft.Stack([
                                ft.Icon(name=ft.icons.DO_NOT_DISTURB_ON_OUTLINED, size=18, color='red')
                            ], alignment=ft.alignment.center),
                            ft.Text('')
                        ])
                       
                else:

                    if i != t:

                        self.l[i].controls[0] = ft.Row([
                            ft.Stack([
                                ft.Icon(name=ft.icons.CHECK_CIRCLE_OUTLINE_ROUNDED, size=18, color='green')
                            ], alignment=ft.alignment.center),
                            ft.Text('')
                        ])
                    else:
                        self.e.padding=0
                        self.e.icon_color=ft.colors.LIGHT_GREEN_ACCENT_100
                        self.e.icon=ft.icons.CHECK_CIRCLE_OUTLINE_ROUNDED
                        
                        
                        self.l[i].controls[0] = ft.Stack([
                            ft.Icon(name=ft.icons.CIRCLE_OUTLINED, size=25, color='blue'),
                            ft.Icon(name=ft.icons.CHECK_CIRCLE_OUTLINE_ROUNDED, size=18, color='green')
                        ], alignment=ft.alignment.center)

            self.inner_content.content.controls.insert(2, self.non)
            self.btnans.content = ft.Text('Выход', size=20, color='black')

            self.btnans.on_click = main1
            self.non.value=self.n
            self.inner_content.padding=10
            page.update()
            time.sleep(0.3)
                # Установить свойства видимости и смещения для нового элемента

            self.non.opacity = 1
            self.non.offset = ft.transform.Offset(0, 0)
            page.update()




    def main3(e):
        global n
        page.clean()
        for i in buts[n]:
            stack.controls.remove(i)

        n=n-1
        if n==-4:
            n=2
        a.offset=ft.transform.Offset(0,0)
        viewcont.content=vs[n]
        page.add(appbar,text,stack)

        for i in buts[n]:
            stack.controls.append(i)

        
        page.update()
        a.offset=ft.transform.Offset(-1,0)
    

    def main4(e):
        global n
        a.offset=ft.transform.Offset(0,0)
        page.clean()

        for i in buts[n]:
            stack.controls.remove(i)
        n+=1
        if n==3:
            n=0
        
        viewcont.content=vs[n]
        page.add(
            appbar,text,stack)
        
        
        for i in buts[n]:
            stack.controls.append(i)
        
        page.update()
        a.offset=ft.transform.Offset(-1,0)
    


   

    def main1(e):
        page.clean()
        

        page.add(appbar,text,stack)
        page.update()
    vid=['вид1.gif','вид2.gif','вид3.gif']
    povorots=['3поворот.gif','','2поворот.gif']
    pov1=['-2поворот.gif','-3поворот.gif','-1поворот.gif']

#vid1

    
    

    v1b1=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(-0.5,-2.2),)
    v1b2=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(-1.04,-0.55),)
    v1b3=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(0.65,0.85),)
    v1b4=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(-0.65,2.05),)
    v1b5=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(1.25,2.92),)
    v1b6=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(-1.64,2.7))
    v1b7=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(2,1.5),)   


    v2b1=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(-0.55,-1.65),)
    v2b2=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(-0.5,0.85),)
    v2b3=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(1.3,0.58),)
    v2b4=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(0.66,3.1),)
    v2b5=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(0.36,2.32),)
    v2b6=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(-1.3,2.98))

    v3b1=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(-0.36,-1.9),)
    v3b2=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(-0.48,-0.69),)
    v3b3=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(-0.05,0.9),)
    v3b4=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(1.28,-0.6),)
    v3b5=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(1.1,3.2),)
    v3b6=ft.IconButton(icon=ft.icons.QUESTION_MARK,rotate=ft.transform.Rotate(0,alignment=ft.alignment.center), icon_color=ft.colors.CYAN_ACCENT_200,offset=(-0.65,3.23))
    lft=ft.IconButton(icon=ft.icons.ARROW_FORWARD_IOS,icon_color=ft.colors.INDIGO_ACCENT_700,offset=(2,0),icon_size=50,on_click=main3)
    rght=ft.IconButton(icon=ft.icons.ARROW_FORWARD_IOS,icon_color=ft.colors.INDIGO_ACCENT_700,offset=(-2,0),icon_size=50,rotate=3.1415,on_click=main4)

    a=ft.Container(bgcolor='green',content=ft.Text(''),height=page.height,width=page.width,offset=ft.transform.Offset(-1,0),
                animate_offset=ft.animation.Animation(800),)
    v1b1cl=we(v1b1)
    v1b2cl=we(v1b2)
    v1b3cl=we(v1b3)
    v1b4cl=we(v1b4)
    v1b5cl=we(v1b5)
    v1b6cl=we(v1b6)
    v1b7cl=we(v1b7)

    v2b1cl=we(v2b1)
    v2b2cl=we(v2b2)
    v2b3cl=we(v2b3)
    v2b4cl=we(v2b4)
    v2b5cl=we(v2b5)
    v2b6cl=we(v2b6)

    v3b1cl=we(v3b1)
    v3b2cl=we(v3b2)
    v3b3cl=we(v3b3)
    v3b4cl=we(v3b4)
    v3b5cl=we(v3b5)
    v3b6cl=we(v3b6)

    
    
    v1b1.on_click=v1b1cl.p
    v1b2.on_click=v1b2cl.p
    v1b3.on_click=v1b3cl.p
    v1b4.on_click=v1b4cl.p
    v1b5.on_click=v1b5cl.p
    v1b6.on_click=v1b6cl.p
    v1b7.on_click=v1b7cl.p

    v2b1.on_click=v2b1cl.p
    v2b2.on_click=v2b2cl.p
    v2b3.on_click=v2b3cl.p
    v2b4.on_click=v2b4cl.p
    v2b5.on_click=v2b5cl.p
    v2b6.on_click=v2b6cl.p

    v3b1.on_click=v3b1cl.p
    v3b2.on_click=v3b2cl.p
    v3b3.on_click=v3b3cl.p
    v3b4.on_click=v3b4cl.p
    v3b5.on_click=v3b5cl.p
    v3b6.on_click=v3b6cl.p
  





    buts=[[v1b1,v1b2,v1b3,v1b4,v1b5,v1b6,v1b7],[v2b1,v2b2,v2b3,v2b4,v2b5,v2b6],[v3b1,v3b2,v3b3,v3b4,v3b5,v3b6]]
   
    viewport=ft.Image(src=vid[0],fit=ft.ImageFit.COVER,filter_quality=ft.FilterQuality.HIGH,border_radius=4, height=500)
    viewpor2=ft.Image(src=vid[1],fit=ft.ImageFit.COVER,filter_quality=ft.FilterQuality.HIGH,border_radius=4, height=500)
    viewpor3=ft.Image(src=vid[2],fit=ft.ImageFit.COVER,filter_quality=ft.FilterQuality.HIGH,border_radius=4, height=500)


    viewpov1=ft.Image(src=povorots[0],fit=ft.ImageFit.COVER,filter_quality=ft.FilterQuality.HIGH,border_radius=4, height=500)
    viewpov2=ft.Image(src=povorots[1],fit=ft.ImageFit.COVER,filter_quality=ft.FilterQuality.HIGH,border_radius=4, height=500)
    viewpov3=ft.Image(src=povorots[2],fit=ft.ImageFit.COVER,filter_quality=ft.FilterQuality.HIGH,border_radius=4, height=500)
    viewpop1=ft.Image(src=pov1[0],fit=ft.ImageFit.COVER,filter_quality=ft.FilterQuality.HIGH,border_radius=4, height=500)
    viewpop2=ft.Image(src=pov1[1],fit=ft.ImageFit.COVER,filter_quality=ft.FilterQuality.HIGH,border_radius=4, height=500)
    viewpop3=ft.Image(src=pov1[2],fit=ft.ImageFit.COVER,filter_quality=ft.FilterQuality.HIGH,border_radius=4, height=500)
    vp=[viewpov1,viewpov2,viewpov3]
    vp1=[viewpop1,viewpop2,viewpop3]
    vs=[viewport,viewpor2,viewpor3]
    viewcont=ft.Container(
        content=viewport,
        image_fit=ft.ImageFit.COVER,
        border_radius=10,
        padding=10,
        image_src='fon_cont.png')
    
    appbar=ft.AppBar(bgcolor=ft.colors.CYAN_ACCENT_200,title=ft.Text(value="Техноелка Т191-24", size=20,weight=ft.FontWeight.BOLD),actions=[

        ])
    
    text=ft.Text('Для активации новогоднего шарика, нажмите на него и ответьте на вопрос.', size=20,offset=(0,-0.1))

    

    stack=ft.Stack([viewcont,lft,rght,v1b1,v1b2,v1b3,v1b4,v1b5,v1b6,v1b7
    ],alignment=ft.alignment.center)



  

    
    main1(1)


        
        
    


ft.app(target=main,view=ft.AppView.WEB_BROWSER,assets_dir=r"assets")