cargo new did_registry
cd did_registry

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_did_registry() {
        let mut registry = DIDRegistry::new();
        registry.register_did(
            "did:example:123".to_string(),
            "key123".to_string(),
            "test metadata".to_string()
        );
        
        let doc = registry.resolve_did(&"did:example:123".to_string());
        assert!(doc.is_some());
    }
}