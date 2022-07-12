# MigrationsExample

https://docs.djangoproject.com/en/3.2/topics/migrations/

## Version control
Because migrations are stored in version control, you’ll occasionally come across situations where you and another developer have both committed a migration to the same app at the same time, resulting in two migrations with the same number.

Don’t worry - the numbers are just there for developers’ reference, Django just cares that each migration has a different name. Migrations specify which other migrations they depend on - including earlier migrations in the same app - in the file, so it’s possible to detect when there’s two new migrations for the same app that aren’t ordered.

When this happens, Django will prompt you and give you some options. If it thinks it’s safe enough, it will offer to automatically linearize the two migrations for you. If not, you’ll have to go in and modify the migrations yourself - don’t worry, this isn’t difficult, and is explained more in Migration files below.

## Dependencies
While migrations are per-app, the tables and relationships implied by your models are too complex to be created for one app at a time. When you make a migration that requires something else to run - for example, you add a ForeignKey in your books app to your authors app - the resulting migration will contain a dependency on a migration in authors.

This means that when you run the migrations, the authors migration runs first and creates the table the ForeignKey references, and then the migration that makes the ForeignKey column runs afterwards and creates the constraint. If this didn’t happen, the migration would try to create the ForeignKey column without the table it’s referencing existing and your database would throw an error.

This dependency behavior affects most migration operations where you restrict to a single app. Restricting to a single app (either in makemigrations or migrate) is a best-efforts promise, and not a guarantee; any other apps that need to be used to get dependencies correct will be.

Apps without migrations must not have relations (ForeignKey, ManyToManyField, etc.) to apps with migrations. Sometimes it may work, but it’s not supported.




