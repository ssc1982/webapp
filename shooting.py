class Person(object):
    """
    class for person
    """

    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name
        self.gun = None
        self.health = 100

    def loadAmmo(self, bullet, ammoClip):
        """
        put bullets into the ammoClip
        :param bullet:
        :param ammoClip:
        :return:
        """
        ammoClip.loadBullet(bullet)

    def insertAmmo(self, gun, ammoCLip):
        """
        insert ammoClip into gun
        :param gun:
        :param ammoCLip:
        :return:
        """
        gun.mountAmmo(ammoCLip)

    def holdGun(self, gun):
        """
        person hold a gun
        :param gun:
        :return:
        """
        self.gun = gun

    def fireShoots(self, enemy):
        """
        start shooting a enemy
        :param enemy:
        :param person:
        :return:
        """
        self.gun.shoot(enemy)

    def loseHealth(self, damage):
        self.health -= damage

    def __str__(self):
        if self.gun:
            return "the health of %s is %s left, he holds a %s in hand" % (self.name, self.health, self.gun)
        else:
            if self.health >0:
                return "the health of %s is %s left, he has no gun in hand" % (self.name, self.health)
            else:
                return "%s has died already" % self.name
class Gun(object):
    """
    class for gun
    """

    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name  # indicate type of gun
        self.ammoList = None

    def mountAmmo(self, ammoClip):
        self.ammoList = ammoClip

    def shoot(self, enemy):
        bullet = self.ammoList.popBullet()
        if bullet:
            bullet.goodShoot(enemy)
        else:
            print("there is no bullet in the ammoClip")

    def __str__(self):
        if self.ammoList:
            return "ammoClip is inserted: %s %s" % (self.name, self.ammoList)
        else:
            return "Type of the gun: %s" % self.name

class AmmoClip(object):
    """
    class for ammo clip
    """

    def __init__(self, max_num):
        super(AmmoClip, self).__init__()
        self.max_num = max_num
        self.bulletList = []

    def loadBullet(self, bullet):
        """
        load the bullets into ammoClip
        :param bullet:
        :return:
        """
        self.bulletList.append(bullet)

    def popBullet(self):
        if self.bulletList:
            return self.bulletList.pop()
        else:
            return None
    def __str__(self):
        return "Bullets in ammoCLip: %d/%d" % (len(self.bulletList), self.max_num)


class Bullet(object):
    """
    class for ammo
    """

    def __init__(self, damage):
        super(Bullet, self).__init__()
        self.damage = damage

    def goodShoot(self, enemy):
        enemy.loseHealth(self.damage)

def main():
    """
    main control function
    :return:
    """
    # 1 create person object
    person = Person("solder")
    # 2 create gun object
    gun = Gun("AK47")
    # 3 create ammo clip object
    ammoClip = AmmoClip(20)
    # 4 create ammo object
    bullet = Bullet(10)
    # 5 create enemy object
    enemy = Person('enemy')
    # 6 person load ammo to ammo clip
    for i in range(1,15):
        bullet = Bullet(10)
        person.loadAmmo(bullet, ammoClip)
    # 7 person put ammo clip into gun
    person.insertAmmo(gun, ammoClip)
    # 8 person hold the gun
    person.holdGun(gun)
    print(person)
    # 9 person kill the enemy
    for i in range(1,11):
        person.fireShoots(enemy)
        print(person)
        print(enemy)


if __name__ == '__main__':
    main()
