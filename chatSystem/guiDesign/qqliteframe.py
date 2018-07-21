# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jul 11 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

loginframe = 1000

###########################################################################
## Class LoginFrame
###########################################################################

class LoginFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = loginframe, title = u"QQLite", pos = wx.DefaultPosition, size = wx.Size( 390,314 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.spacepanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,15 ), wx.TAB_TRAVERSAL )
		bSizer.Add( self.spacepanel, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.mainlabel = wx.StaticText( self, wx.ID_ANY, u"QQLite登录", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.mainlabel.Wrap( -1 )
		
		self.mainlabel.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		
		bSizer.Add( self.mainlabel, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,15 ), wx.TAB_TRAVERSAL )
		bSizer.Add( self.m_panel7, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer101 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"用户名：", wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText111.Wrap( -1 )
		
		self.m_staticText111.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		
		bSizer101.Add( self.m_staticText111, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.user_id_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,30 ), 0 )
		self.user_id_input.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		
		bSizer101.Add( self.user_id_input, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer.Add( bSizer101, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_panel71 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,5 ), wx.TAB_TRAVERSAL )
		bSizer.Add( self.m_panel71, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"   密码：", wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText11.Wrap( -1 )
		
		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		
		bSizer10.Add( self.m_staticText11, 0, 0, 5 )
		
		self.user_pwd_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,30 ), wx.TE_PASSWORD )
		self.user_pwd_input.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		
		bSizer10.Add( self.user_pwd_input, 0, wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer.Add( bSizer10, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_panel711 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,20 ), wx.TAB_TRAVERSAL )
		bSizer.Add( self.m_panel711, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.loginbtn = wx.Button( self, wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.loginbtn.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		
		bSizer14.Add( self.loginbtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.regbtn = wx.Button( self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.regbtn.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		
		bSizer14.Add( self.regbtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer.Add( bSizer14, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.loginbtn.Bind( wx.EVT_LEFT_DOWN, self.loginEvent )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def loginEvent( self, event ):
		event.Skip()
	

