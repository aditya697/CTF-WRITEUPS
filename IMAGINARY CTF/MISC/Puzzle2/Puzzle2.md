# Puzzle2

We are given a `.zip` file which has a game.

In that we can open doors. if we open all doors we can see the flag on some of the wall.

So for that we have to edit source of those pillars using `dnspy` https://github.com/dnSpy/dnSpy/releases

In that by checking all the pillar functions opening ``Assembly-Csharp.dll`` puzzle2 -> puzzle_data -> managed

![image](https://user-images.githubusercontent.com/73250884/127116294-5c339b81-963b-4ba2-80a2-d58c2ea59fa6.png)

I have opened it now checking all the pillars i found `fixedupdate()`

![image](https://user-images.githubusercontent.com/73250884/127116429-8187800b-ee86-45ee-9fc9-da0e6d42731c.png)

Now here in that code 
```
// Pillar
// Token: 0x06000007 RID: 7 RVA: 0x00002153 File Offset: 0x00000353
private void FixedUpdate()
{
	if (!this.stopped)
	{
		base.transform.Translate(this.direction * 0.05f);
	}
}
```

changed to 

Changing this not equal to before this.stopped to equal to this open all the doors in the game.

```
// Pillar
// Token: 0x06000007 RID: 7 RVA: 0x00002153 File Offset: 0x00000353
private void FixedUpdate()
{
	if (this.stopped)
	{
		base.transform.Translate(this.direction * 0.05f);
	}
}
```

Now save file and open the game, this open all the doors at once.

![image](https://user-images.githubusercontent.com/73250884/127117026-71c7fa46-362d-45a1-b735-752223fae93e.png)

FLAG:- ```ICTF{SPY_KIDS_ASSEMBLE}```
