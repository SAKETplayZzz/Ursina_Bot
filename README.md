<p align="center">
<a href="https://github.com/psf/black" rel="nofollow"><img alt="Code style: black" src="https://warehouse-camo.ingress.cmh1.psfhosted.org/fbfdc7754183ecf079bc71ddeabaf88f6cbc5c00/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667"></a>
</p>

# UrsinaBot

## Commands

The bot implements slash commands, type `/` in discord to see them.

| Command | Alias | Arguments | Description                                                                                    | Example     |
| ------- | ----- | --------- | ---------------------------------------------------------------------------------------------- | ----------- |
| `/doc`  |       | LABEL     | Print information from the [`cheat sheet`](https://www.ursinaengine.org/cheat_sheet_dark.html) | `/doc vec3` |


# Hosting

## Docker Compose:

### Steps:

- use the template from [`sample.env`](sample.env) to create an `.env` file
- add your token and other environment variables

## Environment Variables

### Required

- `TOKEN`: The Bot Token used by the bot to authenticate with Discord.

### Optional

- `LOG_LEVEL`: if set to `debug`, the bot will provide additional log messages during operation
- `GUILD_IDS`: a space-separated list of guild ids, these are used to register slash commands for specific test servers
