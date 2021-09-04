# Internal  Processor

```py
def a(v,f): return f"A: {v}"

a(2,3)

..: a(2,3)
  : frame         <frame at 0x00000000027036C0, file '<stdin>', line 1, code <module>>
  : 1 1 <module> <stdin> ('a',) (2, 3, None)
  : co_stacksize        3
  : event         call
  : arg           None

  : frame         <frame at 0x00000000027036C0, file '<stdin>', line 1, code <module>>
  : 1 1 <module> <stdin> ('a',) (2, 3, None)
  : co_stacksize        3
  : event         line
  : arg           None

  : frame         <frame at 0x0000000002703520, file '<stdin>', line 1, code a>
  : 1 1 a <stdin> () (None, 'A: ')
  : co_stacksize        2
  : event         call
  : arg           None

  : frame         <frame at 0x0000000002703520, file '<stdin>', line 1, code a>
  : 1 1 a <stdin> () (None, 'A: ')
  : co_stacksize        2
  : event         line
  : arg           None

  : frame         <frame at 0x0000000002703520, file '<stdin>', line 1, code a>
  : 1 1 a <stdin> () (None, 'A: ')
  : co_stacksize        2
  : event         return
  : arg           A: 2

'A: 2'
  : frame         <frame at 0x00000000027036C0, file '<stdin>', line 1, code <module>>
  : 1 1 <module> <stdin> ('a',) (2, 3, None)
  : co_stacksize        3
  : event         return
  : arg           None

```


```py
def a(v,f): return v+f

  : frame         <frame at 0x000000000056ACC0, file '<stdin>', line 1, code <module>>
  : 1 1 <module> <stdin> ('a',) (<code object a at 0x0000000002706190, file "<stdin>", line 1>, 'a', None)
  : co_stacksize        2
  : event         call
  : arg           None

  : frame         <frame at 0x000000000056ACC0, file '<stdin>', line 1, code <module>>
  : 1 1 <module> <stdin> ('a',) (<code object a at 0x0000000002706190, file "<stdin>", line 1>, 'a', None)
  : co_stacksize        2
  : event         line
  : arg           None

  : frame         <frame at 0x000000000056ACC0, file '<stdin>', line 1, code <module>>
  : 1 1 <module> <stdin> ('a',) (<code object a at 0x0000000002706190, file "<stdin>", line 1>, 'a', None)
  : co_stacksize        2
  : event         return
  : arg           None

a(2,3)

  : frame         <frame at 0x0000000002703520, file '<stdin>', line 1, code <module>>
  : 1 1 <module> <stdin> ('a',) (2, 3, None)
  : co_stacksize        3
  : event         call
  : arg           None

  : frame         <frame at 0x0000000002703520, file '<stdin>', line 1, code <module>>
  : 1 1 <module> <stdin> ('a',) (2, 3, None)
  : co_stacksize        3
  : event         line
  : arg           None

  : frame         <frame at 0x00000000027036C0, file '<stdin>', line 1, code a>
  : 1 1 a <stdin> () (None,)
  : co_stacksize        2
  : event         call
  : arg           None

  : frame         <frame at 0x00000000027036C0, file '<stdin>', line 1, code a>
  : 1 1 a <stdin> () (None,)
  : co_stacksize        2
  : event         line
  : arg           None

  : frame         <frame at 0x00000000027036C0, file '<stdin>', line 1, code a>
  : 1 1 a <stdin> () (None,)
  : co_stacksize        2
  : event         return
  : arg           5

5
  : frame         <frame at 0x0000000002703520, file '<stdin>', line 1, code <module>>
  : 1 1 <module> <stdin> ('a',) (2, 3, None)
  : co_stacksize        3
  : event         return
  : arg           None
```
