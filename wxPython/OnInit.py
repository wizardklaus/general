import wx

class MyApp(wx.App): #wx.App을 상속하는 MyApp 클래스를 정의
    def OnInit(self): #OnInit() 메소드를 오버라이드
        frame=wx.Frame(parent=None,title='Hello!')
        frame.Show(True) #Frame의 인스턴스를 만들어 띄운다
        return True

    if __name__=='__main__':
        app=MyApp()
        app.MainLoop()