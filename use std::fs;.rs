use std::fs;
use serde::Deserialize;

#[derive(Deserialize)]
pub struct Config {
    pub network: NetworkConfig,
}

#[derive(Deserialize)]
pub struct NetworkConfig {
    pub peer_id: String,
    pub listen_address: String,
}

impl Config {
    pub fn new() -> Result<Self, String> {
        let config_str = fs::read_to_string("config.toml")
            .map_err(|e| format!("Error reading config file: {}", e))?;

        let config: Config = toml::from_str(&config_str)
            .map_err(|e| format!("Error parsing config file: {}", e))?;

        Ok(config)
    }
}
